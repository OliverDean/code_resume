use rand::Rng;
use std::cmp::Ordering;
use std::sync::mpsc;
use std::thread;


/// The main function serves as the entry point for the program.
/// 
/// This function orchestrates the following sequence of operations:
/// 
/// 1. **Generate Random Words**:
///     - Generates a list of 1,000 random words, each consisting of 
///       3 to 7 lowercase alphabetic characters.
///     - Prints the first 10 words to provide a sample of the generated data.
/// 
/// 2. **Concurrent Heap Sort**:
///     - Spawns a new thread to perform heap sort on the list of words.
///     - The sorted list is sent back to the main thread via a channel.
/// 
/// 3. **Binary Search**:
///     - Selects a random word from the original list as the search target.
///     - Performs a binary search on the sorted list to determine if the 
///       search target is present.
///     - Prints the position of the search target if found, or a message 
///       indicating that the word was not found.
/// 
/// 4. **Display Sorted Words**:
///     - Prints the first 10 words from the sorted list to demonstrate 
///       the sorting operation.
/// 
/// The program leverages Rust's memory safety, concurrency, and efficient 
/// data handling features, providing a practical example of sorting and 
/// searching operations on a large dataset in a safe and efficient manner.

// Function to generate a list of random words
fn generate_random_words(count: usize) -> Vec<String> {
    let mut rng = rand::thread_rng();
    (0..count)
        .map(|_| {
            let word_len: usize = rng.gen_range(3..8);
            (0..word_len)
                .map(|_| (rng.gen_range(b'a'..=b'z') as char))
                .collect()
        })
        .collect()
}

// Heap sort implementation
fn heap_sort(arr: &mut [String]) {
    let len = arr.len();
    for i in (0..len / 2).rev() {
        heapify(arr, len, i);
    }
    for i in (0..len).rev() {
        arr.swap(0, i);
        heapify(arr, i, 0);
    }
}

fn heapify(arr: &mut [String], len: usize, root: usize) {
    let mut largest = root;
    let left = 2 * root + 1;
    let right = 2 * root + 2;

    if left < len && arr[left] > arr[largest] {
        largest = left;
    }
    if right < len && arr[right] > arr[largest] {
        largest = right;
    }
    if largest != root {
        arr.swap(root, largest);
        heapify(arr, len, largest);
    }
}

// Binary search implementation
fn binary_search(arr: &[String], target: &str) -> Result<usize, usize> {
    let mut low = 0;
    let mut high = arr.len();

    while low < high {
        let mid = (low + high) / 2;
        match arr[mid].as_str().cmp(target) {
            Ordering::Less => low = mid + 1,
            Ordering::Greater => high = mid,
            Ordering::Equal => return Ok(mid),
        }
    }
    Err(low)
}

fn main() {
    // Generate a list of random words
    let word_count = 1000;
    let words = generate_random_words(word_count);

    // Print original words
    println!("Original words: {:?}", &words[..10]);

    let mut words_clone = words.clone();

    // Sort the words using heap sort in a separate thread
    let (tx_sort, rx_sort) = mpsc::channel();
    thread::spawn(move || {
        heap_sort(&mut words_clone);
        tx_sort.send(words_clone).unwrap();
    });

    // Perform a binary search for a random word
    let search_target = words[rand::thread_rng().gen_range(0..words.len())].clone();
    let sorted_words = rx_sort.recv().unwrap();
    match binary_search(&sorted_words, &search_target) {
        Ok(pos) => println!("Found '{}' at position {}", search_target, pos),
        Err(_) => println!("'{}' not found in the list", search_target),
    }

    // Print sorted words
    println!("Sorted words: {:?}", &sorted_words[..10]);
}
