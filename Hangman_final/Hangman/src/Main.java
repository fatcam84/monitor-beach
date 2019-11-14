// Written by Cameron Gifford 11/2/19
// (c) 2019

import java.util.ArrayList;
import java.util.Arrays;
import javax.swing.JOptionPane;
import java.security.SecureRandom;

public class Main {
    private static ArrayList<Character> theWord = new ArrayList<Character>();
    private static ArrayList<Character> correctGuesses = new ArrayList<Character>();
    private static ArrayList<Character> alreadyGuessed = new ArrayList<Character>();
    private static ArrayList<String> wordBank = new ArrayList<String>(
            Arrays.asList("hashbrown", "photograph", "hospital", "understand", "cognitive", "toddler", "lemonade", "canadian", "dolphin", "saltmarsh"));
    private static int numberOfGuesses;
    private static String newWord;

    public static void main(String[] args) {
        pickWord();
        numberOfGuesses = theWord.size() + 6;
        JOptionPane.showMessageDialog(null, "Welcome to Cameron's game of hangman!!\n" +
                "I'm thinking of a word....can you guess it?\nYou can guess 1 lowercase letter at a time and have " + numberOfGuesses + " guesses!!" +
                "\nThink you can figure it out?");
        // System.out.println(theWord.toString());
        playGame();
        if (!correctGuesses.equals(theWord)) {
            JOptionPane.showMessageDialog(null, "Sorry you didn't guess the word in time..." +
                    "\nYou were so close though!!  Do you want to know what the word was?");
            JOptionPane.showMessageDialog(null, "Are you sure???");
            JOptionPane.showMessageDialog(null, "You're positive?");
            JOptionPane.showMessageDialog(null, "Alright, alright the word was...." +
                    "\n" + newWord + "\n" + "Thanks for playing!");
        }
    }

    public static void pickWord() {
        SecureRandom randomNumber = new SecureRandom();
        int randomWord = randomNumber.nextInt(wordBank.size());
        newWord = wordBank.get(randomWord);
        for (int i = 0; i < newWord.length(); i++) {
            theWord.add(i, newWord.charAt(i));
            correctGuesses.add(i, '\u0FD5');
        }
    }


    public static void playGame() {
        for (int counter = 0; counter <= numberOfGuesses; counter++) {
            String toConvert = JOptionPane.showInputDialog(null, "Guess #" + (counter + 1) +
                    "\nPlease guess a letter\nPrevious guesses: " + alreadyGuessed.toString() + "\n" + correctGuesses.toString());
            char guess = toConvert.charAt(0);
            alreadyGuessed.add(counter, guess);

            for (int i = 0; i < theWord.size(); i++) {
                if (guess == theWord.get(i)) {
                    correctGuesses.set(i, guess);
                }
            }
            if (correctGuesses.equals(theWord)) {
                JOptionPane.showMessageDialog(null, "Congratulations!!!!!!\n" +
                        "You've guessed my secret word...." + newWord +
                        "\nAnd it only took you " + counter + " guesses!\nGreat job!");
                break;
            }
        }
    }
}
