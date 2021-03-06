var text;

function setup() {
    noCanvas();

    let bgpage = chrome.extension.getBackgroundPage();
    text = bgpage.word;
    console.log(text);

    var url = 'http://127.0.0.1:5000/extension';
    var postData = {
        "txt": text
    };
    var request = new XMLHttpRequest();
    request.onload = function () {
        var status = request.status;
        var data = request.responseText;
        var level = 0;
        // createP(data).style('font-size', '12pt');
        switch (data) {
            case "Beginner":
                level = 1;
                break;
            case "Intermediate":
                level = 2;
                break;
            case "Advanced":
                level = 3;
                break;
        }
        var lvlctrl = $("#level-control");
        var row = $('<div class="row valign"/>');
        var bubbles = $('<div class="col-md-6 col-sm-6 col-xs-6"/>');
        bubbles.addClass("level-control large level" + level);
        bubbles.append("Level: ");
        renderBubbles(bubbles, level);
        row.append(bubbles);
        var result = $('<div class="alert alert-primary" role="alert">');
        result.append("Reading difficulty : " + data + "</div>");
        var button = $('<button type="button" class="btn btn-primary" id="simplify">simplify</button>');
        lvlctrl.append(row);
        lvlctrl.append(result);
        lvlctrl.append(button);
    }
    request.open("POST", url);
    request.setRequestHeader("Content-Type", "application/json");
    request.send(JSON.stringify(postData));

}

function renderBubbles(lvlctrl, activeLevel) {
    for (var level = 1; level < 4; level++) {
        var isActive = level <= activeLevel;
        var selectedLevel = ' ';
        if (level == activeLevel) selectedLevel = level;
        var activeClass = isActive ? 'active' : '';
        //   console.info("Level " + activeLevel + " " + isActive + " " + selectedLevel);
        var badgeIcon =
            "<span class='fa-stack badge-icon " + activeClass + "'>" +
            " <span>" +
            "   <i class='fa fa-circle fa-stack-2x " + activeClass + "'/>" +
            "   <i class='fa fa-stack-1x badge-icon-text'>" + selectedLevel + "</i>" +
            " </span>" +
            "</span>";
        lvlctrl.append($(badgeIcon));
    }
}

$(document).on('click', '#simplify', function () {
    var url = 'http://127.0.0.1:5000/extension/simplify';
    var postData = {
        "txt": text
    };
    var req = new XMLHttpRequest();
    req.onload = function () {
        var status = req.status;
        var data = req.responseText;
        var result = window.open("", "_blank");
        var doc = result.document;
        doc.open("text/html", "replace");
        doc.write(data);
        doc.close();
    }
    req.open("POST", url);
    req.setRequestHeader("Content-Type", "application/json");
    req.send(JSON.stringify(postData));
});

