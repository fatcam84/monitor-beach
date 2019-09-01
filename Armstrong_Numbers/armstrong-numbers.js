export const validate = (input) => {
  let str = String(input);
  let total = [];
  for (let i = 0; i < str.length; i++) {
    total.push(Math.pow(+str[i], +str.length));
  }
  let realTotal = null;
  total.forEach(number => realTotal += number);
  return realTotal === input ? true: false;
}