import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        System.out.print("Enter vault password: ");
        // String userInput = scanner.next();
        String password = "jU5t_a_sna_3lpm18gb41_u_4_mfr340";

        char[] buffer = new char[32];
        int i;
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        for (i = 16; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i = 8; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }

        
        String s = new String(buffer);
        System.out.println(s);
		// 
	}
}
