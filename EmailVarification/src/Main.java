// Cameron Gifford 11/13/19
// (c) 2019
// List of domains found at https://github.com/mailcheck/mailcheck/wiki/List-of-Popular-Domains
// Complete list of Country Codes http://www.huge.org/clapres/codes.html#organization
import java.util.Scanner;

public class Main {
    public static String email = new String("");
    public static Scanner scan = new Scanner(System.in);
    // 30 most common domain suffix's
    public static String[] domains = {"com", "edu", "gov", "org", "net", "int", "mil", "nato", "uk", "cn", "jp", "fr", "de", "it", "ru",
            "be", "ar", "mx", "ca", "br", "kr", "id", "in", "sg", "ph", "io", "es", "gb", "hk", "ie"};
    public static boolean isDomainTrue = false;

    public static void main(String[] args) {
	    System.out.print("Please enter an email address: ");
	    email = scan.nextLine();
        verifyDomain();
	    if (email.contains("@") && email.contains(".") && isDomainTrue) {
            System.out.println("You have a valid email address!");
        } else {
	        System.out.println("You do not have a valid email address");
	    }
    }

    public static void verifyDomain() {
        for (int i = 0; i < domains.length; i++) {
            if (email.endsWith(domains[i])) {
                isDomainTrue = true;
                break;
            }
        }
        // System.out.println(isDomainTrue);
    }
}
