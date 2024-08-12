pub fn reverse_string(input: &str) -> String {
    input.chars().rev().collect()
}

pub fn bitshift_string(input: &str, shift: u32) -> String {
    input.chars().map(|c| (c as u8).wrapping_add(shift as u8) as char).collect()
}

pub fn to_lower_string(input: &str) -> String {
    input.to_lowercase()
}

pub fn to_upper_string(input: &str) -> String {
    input.to_uppercase()
}

pub fn caesar_cipher(input: &str, shift: u8) -> String {
    input.chars()
        .map(|c| {
            if c.is_ascii_lowercase() {
                (((c as u8 - b'a' + shift) % 26) + b'a') as char
            } else if c.is_ascii_uppercase() {
                (((c as u8 - b'A' + shift) % 26) + b'A') as char
            } else {
                c
            }
        })
        .collect()
}
