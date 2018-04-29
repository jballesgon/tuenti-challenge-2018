import os
from music21 import scale

def get_no_flat_equivalent(self):
    tonic = self.getTonic()
    if tonic.accidental and tonic.accidental.name == 'flat':
        return self.__class__(tonic.getEnharmonic())
    else:
        return self

def to_string(self):
    tonic = self.getTonic()

    return '{mode}{tonic}{modifier}'.format(
        mode = 'M' if isinstance(self, scale.MajorScale) else 'm',
        tonic = tonic.step,
        modifier = tonic.accidental.modifier if tonic.accidental else ''
    )

scale.DiatonicScale.get_no_flat_equivalent = get_no_flat_equivalent
scale.DiatonicScale.__str__ = to_string

def remove_duplicate_scales(scales):
    index = 0
    while index < len(scales) - 1:
        tonic1 = scales[index].getTonic()
        tonic2 = scales[index + 1].getTonic()

        if tonic1.name == tonic2.name:
            del scales[index]
        else:
            index += 1

def parse_and_format_scales(scales):
    no_flat_scales = [sc.get_no_flat_equivalent() for sc in scales]
    sorted_scales = sorted(no_flat_scales, key=lambda sc: sc.getTonic().name)
    remove_duplicate_scales(sorted_scales)

    return [str(sc) for sc in sorted_scales]

def get_fitting_scales_for_tune(notes):
    major_scales = scale.MajorScale().deriveAll(notes)
    minor_scales = scale.MinorScale().deriveAll(notes)

    scales = parse_and_format_scales(major_scales)
    scales.extend(parse_and_format_scales(minor_scales))

    return scales

def get_all_scales():
    pitches = scale.ChromaticScale('A').pitches
    major_scales = [scale.MajorScale(pitch) for pitch in pitches]
    minor_scales = [scale.MinorScale(pitch) for pitch in pitches]

    scales = parse_and_format_scales(major_scales)
    scales.extend(parse_and_format_scales(minor_scales))

    return scales

def main():
    os.chdir(os.path.dirname(__file__))

    input_file = open('submitInput.txt', 'r')
    num_cases = int(input_file.readline())
    output_file = open('submitOutput.txt', 'w')

    for index in range(num_cases):
        num_notes = int(input_file.readline())

        if num_notes == 0:
            scales = get_all_scales()
        else:
            notes = input_file.readline().split()
            scales = get_fitting_scales_for_tune(notes)

        output_file.write('Case #{}: {}\n'.format(
            index + 1,
            ' '.join(scales) if scales else 'None'
        ))

    input_file.close()
    output_file.close()

if __name__ == '__main__':
    main()
