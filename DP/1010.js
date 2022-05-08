const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

let input = [];
let count = 0;
rl.on("line", function (line) {
	input.push(line);
	count++;
	if (count === 2) {
		rl.close();
	}
}).on("close", function () {
	input = input.map((el) => parseInt(el));
	solution(input);
	process.exit();
});

function solution(input) {
	sm = input[0];
	lg = input[1];
	function factorial(n) {
		if (n == 1 || n == 0) {
			return 1;
		} else {
			return n * factorial(n - 1);
		}
	}
	if (sm > lg) {
		return 0;
	} else if (sm === lg) {
		return 1;
	} else {
		return factorial(lg - sm) / (factorial(sm) * factorial(lg));
	}
	const result = solution(lg);
	console.log(result);
}
