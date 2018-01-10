{
  "variables": {
    "conditions": [
      ['OS=="mac"', {"platform": "osx"}],
      ['OS=="win"', {"platform": "win64"}],
      ['OS=="linux"', {"platform": "linux64"}],
    ],
  },
  "targets": [
    {
      "target_name": "flow_parser",
      "sources": [
        "src/flow_parser_node.cc",
      ],
      "include_dirs": [
        "include/",
        "<!(node -e \"require('nan')\")",
      ],
      "libraries": [
        "-L../lib/<(platform)",
        "-lflowparser",
      ],
      "conditions": [
        ['OS=="mac"', {
          "xcode_settings": {
            "OTHER_LDFLAGS": [
              # suppress this warning:
              #   ld: warning: could not create compact unwind for
              #   _caml_start_program: dwarf uses DW_CFA_same_value
              "-Wl,-no_compact_unwind",
            ],
          },
        }],
      ],
    }
  ]
}
