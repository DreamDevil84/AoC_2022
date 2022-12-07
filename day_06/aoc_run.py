def signal_marker(signal, signal_range):
    for i in range(0, len(signal) - signal_range):
        sub_signal = signal[i:i + signal_range]
        has_duplicate = False
        for signal_index in range(0, signal_range - 1):
            if sub_signal[signal_index] in sub_signal[signal_index + 1:]:
                has_duplicate = True
                break
        if not has_duplicate:
            return i + signal_range
    return 0


def part_1(raw_input):
    return signal_marker(raw_input[0], 4)


def part_2(raw_input):
    return signal_marker(raw_input[0], 14)
