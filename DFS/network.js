function solution(n, computers) {
	let visited = [false];
	let answer = 0;

	function dfs(i) {
		visited[i] = true;
		for (let j = 0; j < computers[i].length; j++) {
			console.log(visited, i, "hi");
			if (computers[i][j] === 1 && !visited[j]) {
				dfs(j);
			}
		}
	}
	for (let i = 0; i < computers.length; i++) {
		if (!visited[i]) {
			dfs(i);
			answer++;
		}
	}
	return answer;
}

const computers = [
	[1, 1, 0],
	[1, 1, 0],
	[0, 0, 1],
];

const a = solution(3, computers);
console.log(a);
