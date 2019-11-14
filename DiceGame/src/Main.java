// Written by Cameron Gifford 10/17/19
// (c) 2019

import javax.swing.*;
import java.security.SecureRandom;

public class Main {

    public static final SecureRandom randomNumbers = new SecureRandom();
    static double bank = 0, bet = 0, pot = 0;
    static int die1 = 0, die2 = 0, total = 0;
    static boolean gameInSession = true;

    public static void main(String[] args) {
	    bank = Double.parseDouble(JOptionPane.showInputDialog(null, "Please enter your starting bank amount."));
	    while (gameInSession) {
	        String bankAmnt = String.format("Please enter your bet amount\n(bank: $%.2f)", bank);
	        bet = Double.parseDouble(JOptionPane.showInputDialog(null, bankAmnt));
	        bank -= bet;
	        pot = bet;
	        JOptionPane.showMessageDialog(null, "Rolling the dice....");
	        int roll = rollDice();
	        switch (roll) {
                case 2:
                    JOptionPane.showMessageDialog(null, "SNAKE EYES....loose all your money");
                    bank = 0;
                    gameInSession = false;
                    break;
                case 3:
                case 4:
                case 5:
                case 6:
                    JOptionPane.showMessageDialog(null, "You loose your bet. Better luck next time..");
                    pot = 0;
                    break;
                case 7:
                    JOptionPane.showMessageDialog(null, "You just doubled up!!");
                    bank += (pot + pot);
                    break;
                case 8:
                case 9:
                case 10:
                    JOptionPane.showMessageDialog(null, "You loose your bet. Ugh, so frustrating...");
                    pot = 0;
                    break;
                case 11:
                    JOptionPane.showMessageDialog(null, "Break even. Phew...that was close!");
                    bank += pot;
                    break;
                case 12:
                    JOptionPane.showMessageDialog(null, "Box cars...you loose your bet.");
                    pot = 0;
                    break;
            }

            if (bank > 0) {
                String playAgain = String.format("Do you wish to play again? You still have $%.2f in the bank.\n\nY or N", bank);
                String playAg = JOptionPane.showInputDialog(null, playAgain);
                if (playAg.equals("N")) {
                    gameInSession = false;
                    String goodBye = String.format("Sorry to see you go!\nYou walk away with $%.2f", bank);
                    JOptionPane.showMessageDialog(null, goodBye);
                    break;
                } else {
                    continue;
                }
            } else {
                gameInSession = false;
                JOptionPane.showMessageDialog(null, "Tough loss my friend, hopefully you'll have better luck next time");
            }
        }
    }

    public static int rollDice() {
        die1 = 1 + randomNumbers.nextInt(6);
        die2 = 1 + randomNumbers.nextInt(6);
        total = die1 + die2;
        JOptionPane.showMessageDialog(null, "You rolled " + die1 + " + " + die2 + " = " + total);
        return total;
    }
}
