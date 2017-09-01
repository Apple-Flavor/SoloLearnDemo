import os

    for rt,dirs,files in os.walk("/tmp/test"):
        print rt,dirs,files
