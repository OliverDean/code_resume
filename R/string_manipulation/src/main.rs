mod string_manipulation;

use string_manipulation::{reverse_string, bitshift_string, to_lower_string, to_upper_string, caesar_cipher};

fn main() {
    let input = String::from("thisstringexists");

    // Reverse the string
    let reversed = reverse_string(&input);
    println!("Reversed: {}", reversed);

    // Bitshift the string
    let bitshifted = bitshift_string(&input, 1);
    println!("Bitshifted: {}", bitshifted);

    // Convert to lowercase
    let lowercase = to_lower_string(&input);
    println!("Lowercase: {}", lowercase);

    // Convert to uppercase
    let uppercase = to_upper_string(&input);
    println!("Uppercase: {}", uppercase);

    // Apply Caesar Cipher
    let caesar = caesar_cipher(&input, 4);
    println!("Caesar Cipher (shift 4): {}", caesar);
}
