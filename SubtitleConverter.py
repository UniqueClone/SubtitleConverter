from tkinter import filedialog
from tkinter import messagebox

def srtToVtt(convertee: str, converted: str):
    with open(convertee) as f1, open(converted, 'w') as f2:
        sub_count = 1
        f2.write('WEBVTT\n\n')
        for line in f1:
            if line == str(sub_count) + '\n':
                sub_count += 1
                continue
            elif len(line) == 30 and line[13:16] == '-->':
                f2.write(line[:8] + '.' + line[9:25] + '.' + line[26:])
            else:
                f2.write(line)

def vttToSrt(convertee: str, converted: str):
    with open(convertee) as f1, open(converted, 'w') as f2:
        sub_count = 0
        for line in f1:
            if line == 'WEBVTT\n':
                continue
            elif line == '\n' and sub_count == 0:
                sub_count += 1
                continue
            elif len(line) == 30 and line[13:16] == '-->':
                f2.write(str(sub_count) + '\n')
                sub_count += 1
                f2.write(line[:8] + ',' + line[9:25] + '\n')
            elif line == str(sub_count) + '\n': # sometimes there is already a sub count in the file, we are using our own
                continue
            else:
                f2.write(line)

mode = {
    'srt-to-vtt',
    'vtt-to-srt',
    'error'
}

convertee_path = filedialog.askopenfilename()

convertee = convertee_path
converted = convertee_path[:convertee_path.index('.')]
converted += ".vtt" if convertee.endswith('.srt') else ('.srt')

if convertee.endswith('.srt') and converted.endswith('.vtt'):
    mode = 'srt-to-vtt'
elif convertee.endswith('.vtt') and converted.endswith('.srt'):
    mode = 'vtt-to-srt'
else:
    mode = 'error'

if mode == 'error':
    messagebox.showerror('Error', 'Wrong file extensions. This application only supports SRT -> VTT or VTT -> SRT conversions. Please check your file extensions.')
    # print('Error: Wrong file extensions. This application only supports SRT -> VTT or VTT -> SRT conversions. Please check your file extensions.')
    exit()
elif mode == 'srt-to-vtt':
    print('Converting from SRT to VTT')
    srtToVtt(convertee, converted)
    print('Done!')
elif mode == 'vtt-to-srt':
    print('Converting from VTT to SRT')
    vttToSrt(convertee, converted)
    print('Done!')

