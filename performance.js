

let num_iterations = 1e7;
const list_of_numbers = Array.from(Array(10).keys());
console.log(`Going to perform SUM of the following list, ${num_iterations} times!`);
console.log(list_of_numbers);

let start_time = performance.now();
for (let iteration = 0; iteration < num_iterations; iteration++) {
    let sum = 0;
    for (let index = 0; index < list_of_numbers.length; index++)
        sum += list_of_numbers[index];
}
let end_time = performance.now();
console.log(`It took ${(end_time - start_time) / 1000.0} seconds`);
