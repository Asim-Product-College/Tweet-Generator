$(document).ready(function () {
    $('#refresh').click(getNewTweet);
});

function getNewTweet() {
    fetch('/tweet').then(res => {
        return res.json();
    }).then(json => {
        $('#output').text(json.tweet);
    });
}