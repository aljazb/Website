document.addEventListener('DOMContentLoaded', main, false);

function main() {
	var starGroups = document.getElementsByClassName("stars_group");
	for (var i=0; i < starGroups.length; i++) {
		var starCount = parseInt(starGroups[i].innerHTML);
		starGroups[i].innerHTML = "";
		for (var j=0; j < starCount; j++) {
			starGroups[i].innerHTML += '<img src="/static/images/star.png" alt="Star" class="star_icon">';
		}
	}
}