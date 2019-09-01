export const translate = (rna) => {
  let codons = [];
  if (rna === undefined) {return codons;}
  let splitRNA = rna.match(/\w{3}/g);
  for (let x of splitRNA) {codons.push(x);}
  let pro = [];
  outer: for (let i = 0; i < codons.length; i++) {
    switch (codons[i]) {
      case 'UAA':
      case 'UAG':
      case 'UGA':
        break outer;
      case 'AUG':
        pro.push("Methionine");
        break;
      case 'UUU':
      case 'UUC':
        pro.push("Phenylalanine");
        break;
      case 'UUA':
      case 'UUG':
        pro.push("Leucine");
        break;
      case 'UCU':
      case 'UCC':
      case 'UCA':
      case 'UCG':
        pro.push("Serine");
        break;
      case 'UAU':
      case 'UAC':
        pro.push("Tyrosine");
        break;
      case 'UGU':
      case 'UGC':
        pro.push("Cysteine");
        break;
      case 'UGG':
        pro.push("Tryptophan");
        break;
      default:
        throw new Error("Invalid codon");
    }
  }
  return pro;
}