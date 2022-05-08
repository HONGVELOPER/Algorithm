function solution() {
	let cnt = 0;
	// 그래프 전체 탐색
	for (let i = 0; i < m; i++) {
		for (let j = 0; j < n; j++) {
			//그래프의 값을 돌면서 1이 존재하고 방문한적 없다면
			//해당 위치의 범위에는 DFS가 실행되지 않았으므로 실행
			if (graph[i][j] === 1) {
				DFS(i, j);
				//DFS가 한번 수행되고 나면 해당 노드의 인접노드까지 방문처리가 된다.
				//즉 하나의 배추집단을 파악한 셈이다.
				cnt += 1;
			}
		}
	}
	console.log(cnt);
}

function DFS(i, j) {
	//현재 i,j값이 그래프 범위내인지 검사
	if (RangeCheck(i, j) === true) {
		//현재 위치가 1이고(배추 존재)하고 방문한적없다면
		//방문 처리후 순서대로 DFS
		if (graph[i][j] === 1) {
			graph[i][j] = 0;
			DFS(i + 1, j); //아래
			DFS(i, j + 1); //오른쪽
			DFS(i - 1, j); //위
			DFS(i, j - 1); //왼쪽
		}
	} else {
		return;
	}
}

function RangeCheck(i, j) {
	if (i >= 0 && i < m && j >= 0 && j < n) {
		return true;
	} else return false;
}
