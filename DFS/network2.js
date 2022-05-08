function solution(n, computers) {
	var answer = 0;
	const visited = new Array(n);
	for (let i = 0; i < n; i++) {
		visited[i] = new Array(n);
	}
	console.log(visited, "visit");
	const position = [
		[-1, 0],
		[1, 0],
		[0, -1],
		[0, 1],
	];
	function dfs(r, c) {
		console.log("row : ", r, " col : ", c);
		visited[r][c] = true;
		for (let k = 0; k < position.length; k++) {
			let nr = r + position[k][0];
			let nc = c + position[k][1];
			if (
				nr >= 0 &&
				nr < n &&
				nc >= 0 &&
				nc < n &&
				computers[nr][nc] &&
				!visited[nr][nc]
			) {
				dfs(nr, nc);
			}
		}
	}

	for (let i = 0; i < n; i++) {
		for (let j = 0; j < n; j++) {
			if (computers[i][j] && !visited[i][j]) {
				console.log("==============");
				answer++;
				dfs(i, j);
			}
		}
	}
	return answer;
}

const n = 3;
const computers = [
	[1, 1, 0],
	[1, 1, 0],
	[0, 0, 1],
];
const result = solution(n, computers);
console.log(result);
