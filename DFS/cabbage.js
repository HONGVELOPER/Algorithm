function solution(table) {
	let visited = Array(table.length).fill(0);
	// console.log(visited, "check");
	let answer = 0;

	function dfs(index) {
		console.log("==========================");
		visited[index] = true;
		for (let j = 0; j < table[index].length; j++) {
			console.log(
				"index : ",
				index,
				" j : ",
				j,
				` visit[${j}] : `,
				visited[j]
			);
			if (table[index][j] === 1 && !visited[j]) {
				console.log("진입");
				dfs(j);
			}
		}
	}

	for (let i = 0; i < table.length; i++) {
		console.log(visited, "visit check");
		if (!visited[i]) {
			dfs(i);
			answer += 1;
		}
	}
	console.log("answer : ", answer);
	return answer;
}

// const vertex = 4;
// const line = 5;
// const start = 1;
const table = [
	[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
	[0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
];

solution(table);
