import argparse

from . import dictionary_sample, generate_codenames


def main():
    parser = argparse.ArgumentParser(
        prog="codenamegenerator", description="Code name generator"
    )

    parser.add_argument("num", type=int, default=1)
    parser.add_argument("-c", "--capitalize", action="store_true", default=False)
    parser.add_argument("-t", "--title", action="store_true", default=False)
    parser.add_argument("-s", "--slugify", action="store_true", default=False)

    parser.add_argument("--prefix", help="Prefix dictionary", default="adjectives")

    parser.add_argument(
        "--suffix",
        help="Suffix dictionary",
        default="mobi_notable_scientists_and_hackers",
    )

    args = parser.parse_args()

    for codename in generate_codenames(
        prefix=args.prefix, suffix=args.suffix, num=args.num
    ):
        if args.capitalize:
            codename = codename.capitalize()
        elif args.title:
            codename = codename.title()
        elif args.slugify:
            codename = codename.replace(" ", "_")
        else:
            codename = codename.lower()

        # TODO: support output formats: plain, csv, json, xml
        print(codename)


main()
