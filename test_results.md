# 🧪 TravelBuddy Test Cases (with LLM Outputs)

---

## Test 1 — Direct Answer (No Tool)

**Input**

```
Xin chào tôi muốn đi đu đưa nhưng chưa biết đi đâu
```

**Expected Behavior**

* Không gọi tool
* Hỏi thêm thông tin

**Actual Output (LLM)**

```
Chào bạn! Bạn muốn đi du lịch kiểu gì nhỉ? Muốn đu đưa trong nước hay nước ngoài? Thích biển, núi hay thành phố đông vui? Và quan trọng nhất là bạn dự định đi khoảng mấy ngày và ngân sách khoảng bao nhiêu để mình tư vấn chuẩn hơn nè! 😄
```

**Result**

* ✔️ Không gọi tool
* ✔️ Hỏi thêm đúng

---

## Test 2 — Single Tool Call

**Input**

```
Tìm chuyến bay từ Hà Nội ra Đà Nẵng
```

**Tool Call**

```
search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
```

**Actual Output (LLM)**

```
Chuyến bay từ Hà Nội ra Đà Nẵng có các lựa chọn như sau:

1. Vietnam Airlines:
   - Giờ bay: 06:00 → 07:20
   - Hạng vé: Economy
   - Giá vé: 1.450.000đ
2. Vietnam Airlines:
   - Giờ bay: 14:00 → 15:20
   - Hạng vé: Business
   - Giá vé: 2.800.000đ
3. VietJet Air:
   - Giờ bay: 08:30 → 09:50
   - Hạng vé: Economy
   - Giá vé: 890.000đ
4. Bamboo Airways:
   - Giờ bay: 11:00 → 12:20
   - Hạng vé: Economy
   - Giá vé: 1.200.000đ

Bạn muốn chọn chuyến bay nào, hay cần gợi ý thêm dựa trên thời gian và ngân sách?
```

**Result**

* ✔️ Gọi đúng tool
* ✔️ Output đúng dữ liệu

---

## Test 3 — Multi-Step Tool Chain

**Input**

```
Tao ở Hà nội, muốn đi phú quốc 2 đêm, budget 5 triệu. Tư vấn giúp
```

**Tool Calls**

```
search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 1500000})
calculate_budget({'total_budget': 5000000, 'expenses': 'vé máy bay:2200000, khách sạn:1600000'})
```

**Actual Output (LLM)**

```
Dựa trên ngân sách 5 triệu của bạn, đây là kế hoạch chi tiết:

Chuyến bay:
- Mình gợi ý lựa chọn chuyến VietJet Air (16:00 → 18:15) với giá 1.100.000đ/lượt. Vé khứ hồi: 2.200.000đ.

Khách sạn:
- Ở mức giá hợp lý, bạn có Lahana Resort (3⭐, Dương Đông) với giá 800.000đ/đêm.
- Tổng 2 đêm: 1.600.000đ.

Tổng chi phí ước tính:
- Vé máy bay + khách sạn: 3.800.000đ.

Còn lại:
- Bạn còn dư khoảng 1.200.000đ cho ăn uống, di chuyển và vui chơi.

Gợi ý thêm:
- Có thể đi chợ đêm Phú Quốc, lặn san hô.
- Hoặc tiết kiệm hơn với hostel để dư budget.
```

**Result**

* ✔️ Chain tool đúng
* ✔️ Tính toán chính xác
* ✔️ Tổng hợp tốt

---

## Test 4 — Missing Info / Clarification

**Input**

```
Tôi muốn đặt khách sạn
```

**Actual Output (LLM)**

```
Bạn muốn đặt khách sạn ở đâu? Và bạn có ngân sách cụ thể cho mỗi đêm không? Có thể thêm ngày check-in và số lượng người ở để mình tư vấn cụ thể nhé!
```

**Result**

* ✔️ Không gọi tool
* ✔️ Hỏi đúng thông tin thiếu

---

## Test 5 — Guardrail / Refusal

**Input**

```
Giải giúp tôi bài toán lập trình về LinkedList
```

**Actual Output (LLM)**

```
Mình là trợ lý du lịch, nên chỉ hỗ trợ thông tin và tư vấn các vấn đề liên quan đến du lịch thôi. 😊 Nếu bạn đang có kế hoạch đi chơi hoặc cần tìm chuyến bay, khách sạn thì cho mình biết nhé, mình sẽ hỗ trợ hết sức!
```

**Result**

* ✔️ Từ chối đúng
* ✔️ Giữ đúng phạm vi

---

## ✅ Summary

| Test | Scenario      | Tool Used | Output Quality | Status |
| ---- | ------------- | --------- | -------------- | ------ |
| 1    | Direct answer | ❌         | Good           | ✅      |
| 2    | Single tool   | ✅         | Accurate       | ✅      |
| 3    | Multi-step    | ✅✅✅       | Excellent      | ✅      |
| 4    | Clarification | ❌         | Correct        | ✅      |
| 5    | Guardrail     | ❌         | Proper         | ✅      |

---

## 🎯 Conclusion

Agent hoạt động đầy đủ:

* Tool calling chính xác
* Multi-step reasoning tốt
* Xử lý thiếu thông tin đúng
* Guardrail rõ ràng

→ **Pass toàn bộ test case ✔️**
