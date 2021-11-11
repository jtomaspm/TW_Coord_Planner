from os import times


def build_send_msgs_script(msgs, settings):
    time = settings['time']
    date = settings['date']
    world = settings['world']
    title = settings['title']
    result = ""
    result += "// ==UserScript==\n"
    result += "// @name         send_coord_mail\n"
    result += "// @author       PopAndBoom\n"
    result += "// @match        https://"+world+".tribalwars.com."+world[:2]+"/*&screen=mail*\n"
    result += "// ==/UserScript==\n"
    result += "\n"
    result += "var village_id = window.location.href.match(\"village=\\d*\")[0].split(\"=\")[1];\n"
    result += "\n"
    result += "var players = ["
    players = list(msgs.keys())
    for player in players[:-1]:
        result += "\""+player+"\","
    result += "\"" + players[-1] + "\"];\n"
    result += "var last_name = document.getElementsByClassName(\"nowrap\")[12] == null;\n"
    result += "var last_sent = -1;\n"
    result += "if(!last_name){\n"
    result += "    last_sent = players.indexOf(document.getElementsByClassName(\"nowrap\")[12].children[1].text);\n"
    result += "}\n"
    result += "\n"
    result += "var title = \""+title+"\";\n"
    result += "\n"
    result += "var msgs = [\n"
    for player in players[:-1]:
        first = True
        for zone in msgs[player].keys():
            if first:
                first = False
                result += "     \"[b]Hora: "+ time + "\\nData: " + date + "[/b]\\n\\n\""
            else:
                if not msgs[player][zone] == '':
                    result += "+\"\\n\"+\"\\n\""
            if not msgs[player][zone] == '':
                result += " + \"[spoiler="+zone+"]\\n"+msgs[player][zone]+"[/spoiler]\""
        result +=",\n"
    first = True
    for zone in msgs[player].keys():
        if first:
            first = False
            result += "     \"[b]Hora: "+ time + "\\nData: " + date + "[/b]\\n\\n\""
        else:
            if not msgs[players[-1]][zone] == '':
                result += "+\"\\n\"+\"\\n\""
        if not msgs[players[-1]][zone] == '':
            result += " + \"[spoiler="+zone+"]\\n"+msgs[players[-1]][zone]+"[/spoiler]\\n\""
    result += "\n"
    result += "];\n"   
    result += "\n"
    result += "\n"
    result += "var current_player = last_sent + 1;\n"
    result += "if(current_player >= players.length){\n"
    result += "    console.log(\"Done\");\n"
    result += "}else{\n"
    result += "    myLoop();\n"
    result += "}\n"
    result += "\n"
    result += "function myLoop() {\n"
    result += "    var delay = 1500;\n"
    result += "    setTimeout(function() {\n"
    result += "        $( \"#content_value\" ).load( \"https://"+world+".tribalwars.com.pt/game.php?village=\"+village_id+\"&screen=mail&mode=new\"+ \" #content_value\", function() {\n"
    result += "            console.log(\"Sucess: \" + current_player);\n"
    result += "            document.getElementById(\"to\").value = players[current_player];\n"
    result += "            document.getElementsByName('subject')[0].value = title;\n"
    result += "            document.getElementById(\"message\").value = msgs[current_player];\n"
    result += "            var delay2 = 600;\n"
    result += "            setTimeout(function() {\n"
    result += "                document.getElementsByName('send')[0].click();\n"
    result += "            }, delay2);\n"
    result += "            current_player += 1;\n"
    result += "            myLoop();\n"
    result += "        });\n"
    result += "    }, delay);\n"
    result += "}\n"

    f = open("send_msgs.js", "w")
    f.write(result)
    f.close()

def build_preview_file(plan,zones, settings):
    result = "Hora: " + settings['time'] + "\nData: " + settings['date'] + "\n\n" 
    for player in plan.keys():
        result += player + "\n\n"
        for zone in zones.keys():
            result += zone + "\n\n"
            result += plan[player][zone]
            result += "\n\n"
        
    f = open("preview.txt", "w")
    f.write(result.replace("\\n", "\n"))
    f.close()


