async function getMission() {

const res = await fetch("/api/mission");
const data = await res.json();

document.getElementById("missionBox").innerText = data.mission;

}
