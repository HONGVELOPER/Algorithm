function solution(tickets) {
	var answer = [];
	const visited = [];
	// return answer;
	function dfs(root) {
		for (i = 0; i < tickets.length; i++) {
			if (root === tickets[i][0]) {
				if (tickets[i][0] === "ICN") {
					visited.push(tickets[i][0]);
				}
				if (!visited.includes(tickets[i][1])) {
					visited.push(tickets[i][1]);
				}
				dfs(tickets[i][1]);
			}
		}
	}
	dfs("ICN");
	console.log("visited : " + visited);
}

// solution([
// 	["ICN", "JFK"],
// 	["HND", "IAD"],
// 	["JFK", "HND"],
// ]);

solution([
	["ICN", "SFO"],
	["ICN", "ATL"],
	["SFO", "ATL"],
	["ATL", "ICN"],
	["ATL", "SFO"],
]);
