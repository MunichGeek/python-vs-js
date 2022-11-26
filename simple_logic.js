let words_list = ["axe", "box", "ducks", "lamb"];
for (var word_i of words_list) {
  if (word_i.includes("a") || word_i.includes("b")) {
    console.log(`${word_i} has a or b in it`);
  }
}
