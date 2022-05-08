function solution(n, lost, reserve) {
	var answer = n;
	let count = 0;
	lost.sort();
	for (i of lost) {
		console.log("lost value : ", i);
		if (reserve.includes(i - 1)) {
			console.log("reserve value : ", reserve[reserve.indexOf(i - 1)]);
			reserve[reserve.indexOf(i - 1)] = -1;
		} else if (reserve.includes(i + 1)) {
			console.log("reserve value : ", reserve[reserve.indexOf(i + 1)]);
			reserve[reserve.indexOf(i + 1)] = -1;
			// console.log("포함");
		} else {
			count++;
		}
	}
	console.log("count : ", answer - count);
	return answer - count;
}

const n = 7;
const lost = [3, 4];
// const lost = [3];
const reserve = [1, 2];
// const reserve = [3];
// const reserve = [1];

solution(n, lost, reserve);
