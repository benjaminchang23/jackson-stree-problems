/**
 * BlockingUnorderedMap.h
 * 
 * Thread safe blocking unordered map
 */

#ifndef __BLOCKING_UNORDERED_MAP_H__
#define __BLOCKING_UNORDERED_MAP_H__

#include <functional>
#include <mutex>
#include <unordered_map>

template <typename Key, typename Value, typename Hash = std::hash<Key>>
class BlockingUnorderedMap
{
private:
    std::mutex mutex_;
    std::unordered_map<Key, Value, Hash> map_;
public:
    decltype(auto) begin()
    {
        const std::lock_guard<std::mutex> lock(mutex_);
        map_.begin();
    }

    decltype(auto) emplace(Key key, Value value)
    {
        const std::lock_guard<std::mutex> lock(mutex_);
        return map_.emplace(key, value);
    }

    decltype(auto) erase(Key key)
    {
        const std::lock_guard<std::mutex> lock(mutex_);
        return map_.erase(key);
    }

    decltype(auto) end()
    {
        const std::lock_guard<std::mutex> lock(mutex_);
        map_.end();
    }

    bool find_and_replace(Key key, Value value)
    {
        const std::lock_guard<std::mutex> lock(mutex_);
        if (map_.find(key) == map_.end())
            return false;

        map_.erase(key);

        map_.emplace(key, value);

        return true;
    }

    decltype(auto) find(Key key)
    {
        const std::lock_guard<std::mutex> lock(mutex_);
        return map_.find(key);
    }

    bool count(Key key)
    {
        const std::lock_guard<std::mutex> lock(mutex_);
        return map_.count(key);
    }

    size_t size()
    {
        const std::lock_guard<std::mutex> lock(mutex_);
        size_t size = map_.size();
        return size;
    }

    bool empty()
    {
        const std::lock_guard<std::mutex> lock(mutex_);
        bool check = map_.empty();
        return check;
    }
};

#endif

struct CurrentJobPairHash
{
    std::size_t operator() (const std::pair<const std::string, error_job_rep> &pair) const
    {
        std::size_t h1 = std::hash<std::string>()(pair.first);
        std::size_t h2 = std::hash<error_job_rep>()(pair.second);

        return h1 ^ h2;
    }
};

// other file
BlockingUnorderedMap<std::string>, job_status_t, CurrentJobPairHash> current_jobs_;
