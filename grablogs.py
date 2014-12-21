#!/usr/bin/env python2.6 -B -tt

import os

def main():
    if os.path.isdir("themis.ssl.berkeley.edu/"):
        for root, dirs, files in os.walk("themis.ssl.berkeley.edu/"):
            if len(files) > 0:
                if files[0] == "file_splitter_cmpstats.log":
                    path = "/".join([root, files[0]])
                    if os.path.getsize( path ) > 0:
                        name = root.split("/")[-1].split(".")[-1]
                        os.system( "mkdir -p ~/themis/logs" )
                        os.system( "cp %s ~/themis/logs/%s_cmpstats.log" % (path, name) )
                        print "created: ~/themis/logs/%s_cmpstats.log" % (name,)
    else:
        raise Exception("themis.ssl.berkeley.edu/ directory not found")

if __name__ == "__main__":
    main()
