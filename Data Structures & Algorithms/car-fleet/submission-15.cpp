class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> cars;
        for (int i = 0; i < position.size(); i++) {
            cars.push_back({position[i], speed[i]});
        }
        sort(cars.begin(), cars.end());
        stack<double> carFleets;
        
        for (int i = cars.size() - 1; i >= 0; i--) {
            double time = (double(target) - double(cars[i].first)) / double(cars[i].second);
            // cout << time << endl;
            if (carFleets.empty() || carFleets.top() < time) carFleets.push(time);
        }

        return carFleets.size();
    }
};
