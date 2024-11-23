// https://myactivity.google.com/page?page=youtube_likes&continue=https://myactivity.google.com/product/youtube/interactions

// This string happens to be the div containing the name and URL of the video
Array.prototype.slice.call(document.getElementsByClassName("QTGV3c"))
.filter(
    function(x) {
        return x.innerHTML.startsWith("Liked") //This page displays both liked and disliked videos
    }
).map(
    function(x) {
        return x.children[0]
    }
// Filters out saved playlists and any missing videos
).filter(
    function(x) {
        return !x.innerHTML.startsWith("<div") && !x.innerHTML.startsWith("https://www.youtube.com/watch") && !x.getAttribute("href").includes("playlist")
    }
).map(
    function(x) {
        return {Name: x.innerHTML, URL: x.getAttribute("href")}
    }
)
