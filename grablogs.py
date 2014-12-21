#!/usr/bin/env python2.6 -B -tt

import os

def main():
    for root, dirs, files in os.walk("themis.ssl.berkeley.edu/"):
        print root
        print files
        if len(files) > 0:
            if files[0] == "file_splitter_cmpstats.log":
                path = "/".join([root, files[0]])
                if os.path.getsize( path ) > 0:
                    name = root.split("/")[-1].split(".")[-1]
                    print "name: %s_cmpstats.log" % (name,)
                    os.system( "mkdir -p ~/themis/logs" )
                    os.system( "cp %s ~/themis/logs/%s_cmpstats.log" % (path, name) )

if __name__ == "__main__":
    main()
