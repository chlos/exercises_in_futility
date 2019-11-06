#include <iostream>
#include <string>
#include <vector>


unsigned long long count_hash(std::string& key);

long lookup_key(unsigned long long hash_key, std::vector<unsigned long long>& db_keys);

bool is_offset_collision(long offset, std::vector<unsigned long long>& db_keys);

long insert_key(unsigned long long hash_key, std::vector<unsigned long long>& db_keys, std::vector<long>& db_nums);

std::string get_modified_key(std::string& key, long modifier);


int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    long db_size, entries_number, db_size_coeff = 2;
    std::cin >> entries_number;
    db_size = entries_number * db_size_coeff;

    std::vector<unsigned long long> db_keys(db_size, 0);
    std::vector<long> db_nums(db_size, 0);
    std::string key("");
    long same_keys_num(0);
    for (long i = 0; i < entries_number; ++i) {
        std::cin >> key;
        unsigned long long hash_key = count_hash(key);

        same_keys_num = insert_key(hash_key, db_keys, db_nums);
        if (same_keys_num == 1)
            std::cout << "OK" << '\n';
        else
            std::cout << get_modified_key(key, same_keys_num - 1) << '\n';
    }
}

unsigned long long count_hash(std::string& key)
{
    // http://e-maxx.ru/algo/string_hashes
    const int P = 31;
    unsigned long long hash = 0, p_pow = 1;
    for (unsigned long i = 0; i < key.length(); ++i) {
        hash += (key[i] - 'a' + 1) * p_pow;
        p_pow *= P;
    }
    return hash;
}

long lookup_key(unsigned long long hash_key, std::vector<unsigned long long>& db_keys)
{
    unsigned long offset = hash_key % db_keys.size();
    size_t keys_checked = 0;
    while (keys_checked < db_keys.size()) {
        ++keys_checked;

        // key found or first empty slot found
        if (db_keys[offset] == hash_key || db_keys[offset] == 0)
            return offset;

        if (offset < db_keys.size() - 1)
            ++offset;
        else
            offset = 0;
    }

    return -1;
}

bool is_offset_collision(long offset, std::vector<unsigned long long>& db_keys)
{
    if (db_keys[offset] != 0)
        return true;
    return false;
}

long insert_key(unsigned long long hash_key, std::vector<unsigned long long>& db_keys, std::vector<long>& db_nums)
{
    long offset = lookup_key(hash_key, db_keys);
    if (offset >= 0) {
        db_keys[offset] = hash_key; // in case if we found just first empty slot
        ++db_nums[offset];
    }
    else {
        offset = hash_key % db_keys.size();
        while (is_offset_collision(offset, db_keys))
            if ((unsigned)offset < db_keys.size() - 1)
                ++offset;
            else
                offset = 0;

        db_keys[offset] = hash_key;
        db_nums[offset] = 1;
    }

    return db_nums[offset];
}

std::string get_modified_key(std::string& key, long modifier)
{
    std::string modified_key = key + std::to_string(modifier);
    return modified_key;
}
