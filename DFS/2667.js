let n = 7; // 지도 크기
let answer;
const map = [
	// 단지 정보를 담는 배열
	[0, 1, 1, 0, 1, 0, 0],
	[0, 1, 1, 0, 1, 0, 1],
	[1, 1, 1, 0, 1, 0, 1],
	[0, 0, 0, 0, 1, 1, 1],
	[0, 1, 0, 0, 0, 0, 0],
	[0, 1, 1, 1, 1, 1, 0],
	[0, 1, 1, 1, 0, 0, 0],
];
const visited = new Array(n); // 방문 정보 담는 배열
const result = [];
for (let i = 0; i < visited.length; i++) {
	visited[i] = new Array(n);
}
const position = [
	[-1, 0],
	[1, 0],
	[0, -1],
	[0, 1],
];
// console.log("visited 배열 초기화 : ", visited);

// 깊이 우선 탐색
function dfs(row, col) {
	console.log("행 : ", row + 1, " 열 : ", col + 1);
	answer++;
	visited[row][col] = true;
	// 상, 하, 좌, 우 탐색
	for (let i = 0; i < position.length; i++) {
		let newRow = row + position[i][0];
		let newCol = col + position[i][1];
		if (
			newRow >= 0 &&
			newRow < n &&
			newCol >= 0 &&
			newCol < n &&
			map[newRow][newCol] &&
			!visited[newRow][newCol]
		) {
			dfs(newRow, newCol);
		}
	}
}

function solution() {
	for (let i = 0; i < n; i++) {
		for (let j = 0; j < n; j++) {
			if (map[i][j] == 1 && !visited[i][j]) {
				answer = 0;
				dfs(i, j);
				result.push(answer);
			}
		}
	}
	console.log("단지 수 : ", result.length);
	console.log("결과 값 : ", result);

	return answer;
}

solution();
