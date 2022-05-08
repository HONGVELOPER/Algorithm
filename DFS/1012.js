const map = [
	[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
	[0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
];

const height = 6;
const width = 10;
const num = 17;

const visited = new Array(height);
for (let i = 0; i < height; i++) {
	visited[i] = new Array(width);
}

const position = [
	[-1, 0],
	[1, 0],
	[0, -1],
	[0, 1],
];
let answer = 0;

function dfs(row, col) {
	console.log("행 : ", row + 1, " 열 : ", col + 1);
	visited[row][col] = true;
	for (let i = 0; i < position.length; i++) {
		let nr = row + position[i][0];
		let nc = col + position[i][1];
		if (
			nr >= 0 &&
			nr < height &&
			nc >= 0 &&
			nc < width &&
			map[nr][nc] &&
			!visited[nr][nc]
		) {
			dfs(nr, nc);
		}
	}
}

function solution() {
	for (let i = 0; i < height; i++) {
		for (let j = 0; j < width; j++) {
			if (map[i][j] == 1 && !visited[i][j]) {
				console.log("==========================");
				answer++;
				dfs(i, j);
			}
		}
	}
	return answer;
}

const result = solution();
console.log(result);
