function solution(n, table) {
	let visited = [0];
	let answer = 0;

	function dfs(i, letter) {
		console.log(letter);
		visited[i] = true;

		for (let j = 0; j < table[i].length; j++) {
			console.log("visit : ", i);
			if (table[i][j] === letter && !visited[j]) {
				dfs(j, table[i][j]);
			}
		}
	}
	for (let i = 0; i < n; i++) {
		dfs(i, table[0][0]);
		answer++;
	}
	console.log(answer);
	return answer;
}

const n = 5;
const table = [
	["R", "R", "R", "B", "B"],
	["G", "G", "B", "B", "B"],
	["B", "B", "B", "R", "R"],
	["B", "B", "R", "R", "R"],
	["R", "R", "R", "R", "R"],
];

solution(n, table);
