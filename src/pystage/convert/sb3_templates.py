'''
Rules:
    - Every template ends at the indent_level where it started.
    - At the end of block code add a blank line.
    - New functions (hat blocks) add a newline at the beginning to get to 2 blank lines.
'''

templates = {
        
        "event_whenflagclicked": '''\
                
                def {{func}}_{{ID}}(self):
                    {{NEXT | indent(4)}}

                {{CURRENT_SPRITE}}.{{func}}({{func}}_{{ID}})

                ''',
        
        "event_whenbroadcastreceived": '''\

                def {{func}}_{{ID}}(self):
                    {{NEXT | indent(4)}}

                {{CURRENT_SPRITE}}.{{func}}({{BROADCAST_OPTION}}, {{func}}_{{ID}})

                ''',

        "event_whenkeypressed": '''\

                def {{func}}_{{ID}}(self):
                    {{NEXT | indent(4)}}

                {{CURRENT_SPRITE}}.{{func}}({{KEY_OPTION}}, {{func}}_{{ID}})
                
                ''',

        "event_whenthisspriteclicked": '''\

                def {{func}}_{{ID}}(self):
                    {{NEXT | indent(4)}}

                {{CURRENT_SPRITE}}.{{func}}({{func}}_{{ID}})
                
                ''',

        "event_whenstageclicked": '''\

                def {{func}}_{{ID}}(self):
                    {{NEXT | indent(4)}}

                {{CURRENT_SPRITE}}.{{func}}({{func}}_{{ID}})

                ''',

        "event_whengreaterthan": '''\

                def {{func}}_{{ID}}(self):
                    {{NEXT | indent(4)}}

                {{CURRENT_SPRITE}}.{{func}}({{VALUE}}, {{func}}_{{ID}})

                ''',

        "event_whenbackdropswitchesto": '''\

                def {{func}}_{{ID}}(self):
                    {{NEXT | indent(4)}}

                {{CURRENT_SPRITE}}.{{func}}({{BACKDROP | global_backdrop}}, {{func}}_{{ID}})

                ''',

        "control_start_as_clone": '''\

                def {{func}}_{{ID}}(self):
                    {{NEXT | indent(4)}}

                {{CURRENT_SPRITE}}.{{func}}({{func}}_{{ID}})
                
                ''',

        "control_forever":'''\
                while True:
                    {{SUBSTACK | indent(4)}}
                ''',

        "control_repeat":'''\
                for _ in range({{TIMES | as_int}}):
                    {{SUBSTACK | indent(4)}}
                ''',

        "control_repeat_until": '''\
                while not {{CONDITION}}:
                    {{SUBSTACK | indent(4)}}
                ''',
        
        "control_wait_until": '''\
                while not {{CONDITION}}:
                    pass
                ''',

        "control_if": '''\
                if {{CONDITION | if_missing(False)}}:
                    {{SUBSTACK | indent(4)}}
                ''',

        "control_if_else":'''\
                if {{CONDITION | if_missing(False)}}:
                    {{SUBSTACK | indent(4)}}
                else:
                    {{SUBSTACK2 | indent(4)}}
                ''',

        "operator_add": "({{NUM1}} + {{NUM2}})",
        "operator_and": "({{OPERAND1 | if_missing(False)}} and {{OPERAND2 | if_missing(False)}})",
        "operator_contains": "self.{{func}}({{STRING1}}, {{STRING2}})",
        "operator_divide": "({{NUM1}} / {{NUM2}})",
        "operator_equals": "({{OPERAND1}} == {{OPERAND2}})",
        "operator_gt": "({{OPERAND1}} > {{OPERAND2}})",
        "operator_join": "self.{{func}}({{STRING1}}, {{STRING2}})",
        "operator_length": "self.{{func}}({{STRING}})",
        "operator_letter_of": "self.{{func}}({{LETTER}}, {{STRING}})",
        "operator_lt": "({{OPERAND1}} < {{OPERAND2}})",
        "operator_mod": "({{NUM1}} % {{NUM2}})",
        "operator_multiply": "({{NUM1}} * {{NUM2}})",
        "operator_not": "not ({{OPERAND | if_missing(False)}})",
        "operator_or": "({{OPERAND1 | if_missing(False)}} or {{OPERAND2 | if_missing(False)}})",
        "operator_round": "self.{{func}}({{NUM}})",
        "operator_random": "self.{{func}}({{FROM}}, {{TO}})",
        "operator_mathop": "self.{{func}}({{OPERATOR}}, {{NUM}})",

        "data_addtolist": "self.{{func}}({{LIST}}, {{ITEM}})",
        "data_deleteoflist": "self.{{func}}({{LIST}}, {{INDEX}})",
        "data_insertatlist": "self.{{func}}({{LIST}}, {{ITEM}}, {{INDEX}})",
        "data_replaceitemoflist": "self.{{func}}({{LIST}}, {{INDEX}}, {{ITEM}})",
        "data_itemoflist": "self.{{func}}({{LIST}}, {{INDEX}})",
        "data_itemnumoflist": "self.{{func}}({{LIST}}, {{ITEM}})",
        "data_listcontainsitem": "self.{{func}}({{LIST}}, {{ITEM}})",
        "data_setvariableto": "self.{{func}}({{VARIABLE}}, {{VALUE}})",
        "data_changevariableby": "self.{{func}}({{VARIABLE}}, {{VALUE}})",

        "motion_glidesecstoxy": "self.{{func}}({{SECS}}, {{X}}, {{Y}})",
        "motion_gotoxy": "self.{{func}}({{X}}, {{Y}})",
        "looks_sayforsecs": "self.{{func}}({{MESSAGE}}, {{SECS}})",
        "looks_thinkforsecs": "self.{{func}}({{MESSAGE}}, {{SECS}})",
        "sensing_coloristouchingcolor": "self.{{func}}({{COLOR}}, {{COLOR2}})",
        "operator_subtract": "({{NUM1}} - {{NUM2}})",

        "looks_costume": "{{COSTUME | global_costume}}",
        "looks_backdrops": "{{BACKDROP | global_backdrop}}",

        "sensing_keyoptions": "{{KEY_OPTION}}",
        "sensing_distancetomenu": "{{DISTANCETOMENU | global_sprite}}",
        "sensing_touchingobjectmenu": "{{TOUCHINGOBJECTMENU | global_sprite}}",
        "control_create_clone_of_menu": "{{CLONE_OPTION | global_sprite }}",
        "sensing_of_object_menu": "{{OBJECT | global_sprite }}",
        "motion_pointtowards_menu": "{{TOWARDS | global_sprite }}",
        "motion_goto_menu": "{{TO | global_sprite }}",
        "motion_glideto_menu": "{{TO | global_sprite }}",
        "pen_menu_colorParam": "{{colorParam}}",
        "sound_sounds_menu": "{{SOUND_MENU | global_sound }}",
                }


