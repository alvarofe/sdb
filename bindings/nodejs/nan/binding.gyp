{
  "targets": [
    {
      "type": "none",
      "target_name": "sdb",
      "sources": [ "sdb.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
	"./lib/sdb/src"
      ],
      "dependencies": [
        "./lib/sdb.gyp:libsdb"
      ]
    }
  ]
}
