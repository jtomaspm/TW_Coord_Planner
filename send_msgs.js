// ==UserScript==
// @name         send_coord_mail
// @author       PopAndBoom
// @match        https://pt76.tribalwars.com.pt/*&screen=mail*
// ==/UserScript==

var village_id = window.location.href.match("village=\d*")[0].split("=")[1];

var players = ["mialou11","PekZeus","pay2win?","damapatuxa","rjbeast","cavador10","JotaCe","filipemn","- L0rdRAD"];
var last_name = document.getElementsByClassName("nowrap")[12] == null;
var last_sent = -1;
if(!last_name){
    last_sent = players.indexOf(document.getElementsByClassName("nowrap")[12].children[1].text);
}

var title = "Coordenado";

var msgs = [
     "[b]Hora: 12:00:00\nData: 23/03/2022[/b]\n\n" + "[spoiler=Zona1]\n433|405 : 5 fulls \n433|403 : 5 fulls \n434|405 : 5 fulls \n435|405 : 5 fulls \n435|406 : 5 fulls \n434|407 : 5 fulls \n436|407 : 2 fulls \n[/spoiler]"+"\n"+"\n" + "[spoiler=Fakes]\n449|549 : 7 fulls \n457|547 : 7 fulls \n500|569 : 4 fulls \n445|551 : 7 fulls \n506|576 : 5 fulls \n[/spoiler]",
     "[b]Hora: 12:00:00\nData: 23/03/2022[/b]\n\n" + "[spoiler=Zona1]\n436|407 : 3 fulls \n434|408 : 5 fulls \n434|409 : 5 fulls \n431|405 : 5 fulls \n[/spoiler]"+"\n"+"\n" + "[spoiler=Fakes]\n506|576 : 2 fulls \n502|568 : 7 fulls \n503|567 : 7 fulls \n449|557 : 5 fulls \n507|576 : 7 fulls \n493|571 : 2 fulls \n[/spoiler]",
     "[b]Hora: 12:00:00\nData: 23/03/2022[/b]\n\n" + "[spoiler=Zona1]\n439|407 : 5 fulls \n439|409 : 1 fulls \n[/spoiler]"+"\n"+"\n" + "[spoiler=Fakes]\n495|570 : 7 fulls \n486|555 : 7 fulls \n493|562 : 7 fulls \n493|569 : 7 fulls \n449|557 : 2 fulls \n[/spoiler]",
     "[b]Hora: 12:00:00\nData: 23/03/2022[/b]\n\n" + "[spoiler=Zona1]\n439|409 : 4 fulls \n437|409 : 5 fulls \n435|411 : 3 fulls \n[/spoiler]"+"\n"+"\n" + "[spoiler=Fakes]\n493|571 : 5 fulls \n495|564 : 7 fulls \n505|559 : 7 fulls \n454|546 : 7 fulls \n449|551 : 4 fulls \n[/spoiler]",
     "[b]Hora: 12:00:00\nData: 23/03/2022[/b]\n\n"+"\n"+"\n" + "[spoiler=Zona2]\n496|436 : 4 fulls \n495|436 : 4 fulls \n491|439 : 4 fulls \n491|441 : 4 fulls \n489|442 : 4 fulls \n488|442 : 4 fulls \n487|442 : 4 fulls \n486|439 : 4 fulls \n486|438 : 4 fulls \n488|435 : 4 fulls \n488|436 : 4 fulls \n486|434 : 4 fulls \n490|444 : 2 fulls \n[/spoiler]"+"\n"+"\n" + "[spoiler=Fakes]\n470|545 : 6 fulls \n478|532 : 7 fulls \n502|588 : 7 fulls \n477|568 : 7 fulls \n500|569 : 3 fulls \n[/spoiler]",
     "[b]Hora: 12:00:00\nData: 23/03/2022[/b]\n\n"+"\n"+"\n" + "[spoiler=Zona2]\n490|444 : 2 fulls \n491|444 : 4 fulls \n490|445 : 4 fulls \n488|445 : 4 fulls \n487|446 : 4 fulls \n486|447 : 2 fulls \n[/spoiler]"+"\n"+"\n" + "[spoiler=Zona3]\n550|613 : 3 fulls \n553|616 : 8 fulls \n554|616 : 8 fulls \n556|615 : 1 fulls \n[/spoiler]"+"\n"+"\n" + "[spoiler=Fakes]\n453|550 : 7 fulls \n452|545 : 7 fulls \n501|564 : 7 fulls \n451|548 : 7 fulls \n477|541 : 2 fulls \n[/spoiler]",
     "[b]Hora: 12:00:00\nData: 23/03/2022[/b]\n\n"+"\n"+"\n" + "[spoiler=Zona2]\n486|447 : 2 fulls \n489|448 : 4 fulls \n490|449 : 4 fulls \n491|448 : 2 fulls \n[/spoiler]"+"\n"+"\n" + "[spoiler=Zona3]\n556|615 : 7 fulls \n560|615 : 8 fulls \n559|613 : 8 fulls \n557|609 : 7 fulls \n[/spoiler]"+"\n"+"\n" + "[spoiler=Fakes]\n481|539 : 3 fulls \n462|555 : 7 fulls \n470|543 : 7 fulls \n447|545 : 7 fulls \n483|535 : 6 fulls \n[/spoiler]",
     "[b]Hora: 12:00:00\nData: 23/03/2022[/b]\n\n"+"\n"+"\n" + "[spoiler=Zona2]\n491|448 : 2 fulls \n494|448 : 4 fulls \n507|385 : 6 fulls \n508|385 : 6 fulls \n507|386 : 6 fulls \n505|386 : 3 fulls \n[/spoiler]"+"\n"+"\n" + "[spoiler=Zona3]\n553|611 : 2 fulls \n550|612 : 8 fulls \n550|613 : 5 fulls \n[/spoiler]"+"\n"+"\n" + "[spoiler=Fakes]\n477|541 : 5 fulls \n448|550 : 7 fulls \n470|538 : 7 fulls \n456|567 : 7 fulls \n481|539 : 4 fulls \n[/spoiler]",
     "[b]Hora: 12:00:00\nData: 23/03/2022[/b]\n\n"+"\n"+"\n" + "[spoiler=Zona3]\n557|612 : 8 fulls \n558|613 : 8 fulls \n556|614 : 8 fulls \n555|614 : 8 fulls \n555|613 : 8 fulls \n555|611 : 8 fulls \n557|610 : 8 fulls \n556|610 : 8 fulls \n553|611 : 6 fulls \n[/spoiler]\n"+"\n"+"\n" + "[spoiler=Fakes]\n532|577 : 7 fulls \n501|569 : 7 fulls \n483|535 : 1 fulls \n459|568 : 7 fulls \n445|548 : 7 fulls \n470|545 : 1 fulls \n[/spoiler]\n"
];


var current_player = last_sent + 1;
if(current_player >= players.length){
    console.log("Done");
}else{
    myLoop();
}

function myLoop() {
    var delay = 1500;
    setTimeout(function() {
        $( "#content_value" ).load( "https://pt76.tribalwars.com.pt/game.php?village="+village_id+"&screen=mail&mode=new"+ " #content_value", function() {
            console.log("Sucess: " + current_player);
            document.getElementById("to").value = players[current_player];
            document.getElementsByName('subject')[0].value = title;
            document.getElementById("message").value = msgs[current_player];
            var delay2 = 600;
            setTimeout(function() {
                document.getElementsByName('send')[0].click();
            }, delay2);
            current_player += 1;
            myLoop();
        });
    }, delay);
}
