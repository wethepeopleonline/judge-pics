import hashlib
import json
import os
import subprocess


operating_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(os.path.join(operating_directory, 'orig'))

judges_json = json.load(open('../judges.json', 'r'))


def get_old_hash(image):
    """Get the old hash from seals.json"""
    return judges_json.get(image.split('.')[0], {}).get('hash')


def get_hash_from_file(image):
    """Get the hash from the current file"""
    with open(image, 'r') as f:
        return hashlib.sha256(f.read()).hexdigest()


def set_new_hash(judge_id, new_hash):
    """Update the json object with new values"""
    try:
        judges_json[judge_id]['hash'] = new_hash
    except KeyError:
        judges_json[judge_id] = {
            "hash": new_hash,
            "license": "Work of Federal Government",
            "source": None,
            "artist": None,
            "date_created": None,
        }


def convert_images():
    for image in os.listdir('.'):
        print "\nProcessing: %s" % image
        judge_id = image.split('.')[0]
        final_name = '%s.jpeg' % judge_id
        current_hash = get_hash_from_file(image)
        old_hash = get_old_hash(image)
        if current_hash != old_hash:
            # Update the hash
            set_new_hash(judge_id, current_hash)

            # Regenerate the images
            for size in ['128', '256', '512', '1024']:
                print "  - Making {size}x{size} image...".format(size=size)
                command = [
                    'convert',
                    '-resize',
                    '%sx%s' % (size, size),
                    '-background',
                    'transparent',
                    image,
                    '../%s/%s' % (size, final_name),
                ]
                subprocess.Popen(command, shell=False).communicate()
        else:
            print ' - Unchanged hash, moving on.'


def save_new_json():
    """Update the JSON object on disk."""
    json.dump(
        judges_json,
        open('../judges.json', 'w'),
        sort_keys=True,
        indent=2,
    )

if __name__ == '__main__':
    convert_images()
    save_new_json()
