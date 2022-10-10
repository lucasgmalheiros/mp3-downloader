import argparse
import yt_dlp
import os

parser = argparse.ArgumentParser()
parser.add_argument('link', type=str, help='YouTube video link')
parser.add_argument('-o', '--output', type=str,
                    help='Download folder (Default: Music)',
                    default=f'C:/Users/{os.getlogin()}/Music')
args = parser.parse_args()
link = args.link
path = args.output

def format_path(p):
    """Prepares a Windows' path to receive the downloaded mp3"""
    p = os.path.normpath(p).split(os.path.sep)
    p.append('{}')
    p = '/'.join(p)
    return p

def download(url, p):
    """Executes the download receiving a YouTube link and a system path to save the mp3"""
    execute = True
    info = yt_dlp.YoutubeDL().extract_info(url=url, download=False)
    file_name = '{}.mp3'.format(info['title'])
    p = format_path(p)
    options = {
        'format': 'bestaudio/best',
        'outtmpl': p.format(file_name),
        'keepvideo': True
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
    except:
        execute = False

    return execute


if __name__ == '__main__':
    download(link, path)
