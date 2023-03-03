class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {

        // <name, accounts>
        unordered_map<string, vector<vector<string>>> m;

        for (int i = 0; i < accounts.size(); i++) {
            string name = accounts[i][0];
            auto emails = vector<string>(accounts[i].begin()+1, accounts[i].end());

            if (m.find(name) == m.end()) {
                m[name].push_back(
                    emails
                );
            }
            else {
                m[name] = _merge(
                    m[name],
                    emails
                );
            }
        }

        vector<vector<string>> ans;
        for (const auto & ptr: m) {
            auto name = ptr.first;
            auto emails_list = ptr.second;
            for (auto & emails : emails_list) {
                _deduplicate(emails);
                sort(emails.begin(), emails.end());
                emails.insert(emails.begin(), name);
                ans.push_back(emails);
            }
        }
        return ans;
    }
    static bool compare(string email1, string email2) {
        return email1 < email2;
    }
private:
    void _deduplicate(vector<string>& list) {
        set<string> s;
        for (const auto & item : list) {
            s.insert(item);
        }
        list.clear();
        for (const auto & item : s) {
            list.push_back(item);
        }
    }

    vector<vector<string>> _merge(
        vector<vector<string>>& emails_list,
        vector<string>& target_emails
    ) {
        vector<int> overlay_idxs;
        for (int i = 0; i < emails_list.size(); i++) {
            auto & emails = emails_list[i];
            if (_is_overlay(emails, target_emails)) {
                overlay_idxs.push_back(i);
            }
        }


        vector<vector<string>> ret;
        for (int i = 0; i < emails_list.size(); i++) {
            auto & emails = emails_list[i];

            if (
                find(overlay_idxs.begin(), overlay_idxs.end(), i) != overlay_idxs.end()
            ) {
                _merge_two_emails(target_emails, emails);
            }
            else {
                ret.push_back(emails);
            }
        }
        ret.push_back(target_emails);
        return ret;
    }

    
    bool _is_overlay(vector<string>& emails1, vector<string>& emails2) {
        for (auto & email : emails1) {
            if (
                find(emails2.begin(), emails2.end(), email) != emails2.end()
            ) {
                return true;
            }
        }
        return false;
    }
    void _merge_two_emails(vector<string>& emails1, vector<string>& emails2) {
        emails1.insert(emails1.end(), emails2.begin(), emails2.end());
    }
};