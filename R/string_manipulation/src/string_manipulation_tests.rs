#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_reverse_string() {
        let input = "hello";
        assert_eq!(reverse_string(input), "olleh");
    }

    #[test]
    fn test_bitshift_string() {
        let input = "abc";
        assert_eq!(bitshift_string(input, 1), "bcd");
    }

    #[test]
    fn test_to_lower_string() {
        let input = "HELLO";
        assert_eq!(to_lower_string(input), "hello");
    }

    #[test]
    fn test_to_upper_string() {
        let input = "hello";
        assert_eq!(to_upper_string(input), "HELLO");
    }

    #[test]
    fn test_caesar_cipher() {
        let input = "hello";
        assert_eq!(caesar_cipher(input, 4), "lipps");
    }
}
