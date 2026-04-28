from agent import diagnose

test_cases = [
    "op-amp output stuck high",
    "no current in circuit",
    "noisy signal on oscilloscope"
]

def run_tests():
    passed = 0

    for test in test_cases:
        print(f"\nTesting: {test}")
        result = diagnose(test)

        if result and len(result) > 20:
            print("✅ Passed")
            passed += 1
        else:
            print("❌ Failed")

    print(f"\n{passed}/{len(test_cases)} tests passed")

if __name__ == "__main__":
    run_tests()
