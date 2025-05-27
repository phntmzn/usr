#!/usr/bin/env python3
from flask import Flask, request, render_template_string, send_file
import io
import struct

app = Flask(__name__)

# HTML form for uploading a MIDI file
HTML_FORM = """
<!doctype html>
<title>Upload MIDI File</title>
<h1>Upload a .mid file</h1>
<form method=post enctype=multipart/form-data>
    <input type=file name=midi>
    <input type=submit value=Upload>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def upload_midi():
        # Handle file upload via POST
        if request.method == "POST":
                midi_file = request.files["midi"]
                if not midi_file.filename.endswith(".mid"):
                        return "Please upload a valid .mid file"

                data = midi_file.read()
                patterns = parse_midi_binary(data)  # Parse MIDI file for drum patterns
                code = generate_function_code("drumpatterns", patterns)  # Generate Python code

                # Send generated code as a downloadable file
                return send_file(
                        io.BytesIO(code.encode()),
                        mimetype="text/plain",
                        as_attachment=True,
                        download_name="drumpatterns.py"
                )

        # If GET request, render the upload form
        return render_template_string(HTML_FORM)

def read_variable_length(data, index):
        """
        Reads a MIDI variable-length value starting at data[index].
        Returns (value, new_index).
        """
        result = 0
        while True:
                byte = data[index]
                result = (result << 7) | (byte & 0x7F)
                index += 1
                if byte & 0x80 == 0:
                        break
        return result, index

def parse_midi_binary(data):
        """
        Parses MIDI binary data and extracts note-on events as drum patterns.
        Returns a dictionary mapping note numbers to lists of (note, time) tuples.
        """
        patterns = {}
        index = 0

        # Check MIDI header
        if data[0:4] != b'MThd':
                raise ValueError("Not a valid MIDI file")

        index += 8  # Skip 'MThd' + header length
        index += 6  # Skip format, num tracks, division

        while index < len(data):
                if data[index:index+4] != b'MTrk':
                        break

                track_length = struct.unpack(">I", data[index+4:index+8])[0]
                index += 8
                track_end = index + track_length
                abs_time = 0
                last_status = None

                while index < track_end:
                        # Read delta time
                        delta_time, index = read_variable_length(data, index)
                        abs_time += delta_time

                        status_byte = data[index]
                        if status_byte < 0x80:
                                # Running status: reuse last status byte
                                status = last_status
                        else:
                                index += 1
                                status = status_byte
                                last_status = status

                        if status >= 0x90 and status <= 0x9F:
                                # Note on event
                                note = data[index]
                                velocity = data[index+1]
                                index += 2
                                if velocity > 0:
                                        patterns.setdefault(note, []).append((note, abs_time))
                        elif status >= 0x80 and status <= 0x8F:
                                # Note off event
                                index += 2
                        elif status == 0xFF:
                                # Meta event: skip over it
                                meta_type = data[index]
                                index += 1
                                length, index = read_variable_length(data, index)
                                index += length
                        else:
                                # Other MIDI event (e.g., control change): skip 2 bytes
                                index += 2

        return patterns

def generate_function_code(func_name, patterns):
        """
        Generates Python code for a function that creates drum MIDI files
        from the extracted patterns.
        """
        lines = [f"def {func_name}():", '    folder = base_folder\n']
        for i, (note, sequence) in enumerate(patterns.items()):
                var = f"pattern_{i}"
                lines.append(f"    {var} = [")
                for note_val, time in sequence:
                        lines.append(f"        ({note_val}, {time}),")
                lines.append("    ]")
                lines.append(f"    create_drum_midi(folder / '{var}.mid', {var}, channel=1)\n")
        return "\n".join(lines)


if __name__ == "__main__":
        app.run(debug=True)
