#!/usr/bin/env python3
"""
Test the Figma to Elementor conversion with real data
"""

import json
from parsers.figma_parser import FigmaParser
from generators.elementor_generator import ElementorGenerator

# Your actual Figma data
figma_data = {"id":"1:2","name":"Slide 16:9 - 1","type":"FRAME","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#fafaf7"}],"absoluteBoundingBox":{"x":0,"y":0,"width":1440,"height":2180},"children":[{"id":"1:3","name":"Navigation","type":"FRAME","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#fafaf7"}],"absoluteBoundingBox":{"x":0,"y":0,"width":1440,"height":80},"children":[]},{"id":"1:5","name":"Nav Services","type":"TEXT","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#4d4d4d"}],"absoluteBoundingBox":{"x":900,"y":30,"width":66,"height":19},"characters":"Services","style":{"fontFamily":"Inter","fontStyle":"Regular","fontWeight":400,"fontSize":16,"textAlignHorizontal":"LEFT","letterSpacing":0,"lineHeightPx":19.363636016845703}},{"id":"1:6","name":"Nav About","type":"TEXT","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#4d4d4d"}],"absoluteBoundingBox":{"x":1000,"y":30,"width":46,"height":19},"characters":"About","style":{"fontFamily":"Inter","fontStyle":"Regular","fontWeight":400,"fontSize":16,"textAlignHorizontal":"LEFT","letterSpacing":0,"lineHeightPx":19.363636016845703}},{"id":"1:7","name":"Nav Work","type":"TEXT","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#4d4d4d"}],"absoluteBoundingBox":{"x":1080,"y":30,"width":39,"height":19},"characters":"Work","style":{"fontFamily":"Inter","fontStyle":"Regular","fontWeight":400,"fontSize":16,"textAlignHorizontal":"LEFT","letterSpacing":0,"lineHeightPx":19.363636016845703}},{"id":"1:8","name":"CTA Button Nav","type":"FRAME","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#0485b2"}],"cornerRadius":24,"absoluteBoundingBox":{"x":1200,"y":22,"width":140,"height":40},"children":[]},{"id":"1:9","name":"CTA Nav Text","type":"TEXT","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#ffffff"}],"absoluteBoundingBox":{"x":1230,"y":32,"width":78,"height":17},"characters":"Get Started","style":{"fontFamily":"Inter","fontStyle":"Medium","fontWeight":500,"fontSize":14,"textAlignHorizontal":"LEFT","letterSpacing":0,"lineHeightPx":16.94318199157715}},{"id":"1:10","name":"Hero Section","type":"FRAME","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#fafaf7"}],"absoluteBoundingBox":{"x":0,"y":80,"width":1440,"height":700},"children":[]},{"id":"1:11","name":"Hero Title 1","type":"TEXT","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#1a1a1a"}],"absoluteBoundingBox":{"x":80,"y":180,"width":522,"height":87},"characters":"We help brands","style":{"fontFamily":"Inter","fontStyle":"Light","fontWeight":300,"fontSize":72,"textAlignHorizontal":"LEFT","letterSpacing":0,"lineHeightPx":87.13636016845703}},{"id":"1:12","name":"Hero Title 2","type":"TEXT","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#1a1a1a"}],"absoluteBoundingBox":{"x":80,"y":260,"width":603,"height":87},"characters":"dominate search.","style":{"fontFamily":"Inter","fontStyle":"Semi Bold","fontWeight":600,"fontSize":72,"textAlignHorizontal":"LEFT","letterSpacing":0,"lineHeightPx":87.13636016845703}},{"id":"1:13","name":"Hero Subtitle","type":"TEXT","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#737373"}],"absoluteBoundingBox":{"x":80,"y":380,"width":472,"height":48},"characters":"Strategic SEO solutions that drive organic growth,\nincrease visibility, and deliver measurable results.","style":{"fontFamily":"Inter","fontStyle":"Regular","fontWeight":400,"fontSize":20,"textAlignHorizontal":"LEFT","letterSpacing":0,"lineHeightPx":24.204544067382812}},{"id":"1:14","name":"Hero CTA Button","type":"FRAME","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#0485b2"}],"cornerRadius":28,"absoluteBoundingBox":{"x":80,"y":480,"width":180,"height":56},"children":[]},{"id":"1:15","name":"Hero Secondary Button","type":"FRAME","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#fafaf7"}],"strokes":[{"blendMode":"NORMAL","type":"SOLID","color":"#0485b2"}],"cornerRadius":28,"absoluteBoundingBox":{"x":280,"y":480,"width":180,"height":56},"children":[]},{"id":"1:16","name":"Hero CTA Text","type":"TEXT","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#ffffff"}],"absoluteBoundingBox":{"x":120,"y":496,"width":110,"height":19},"characters":"Start a Project","style":{"fontFamily":"Inter","fontStyle":"Medium","fontWeight":500,"fontSize":16,"textAlignHorizontal":"LEFT","letterSpacing":0,"lineHeightPx":19.363636016845703}},{"id":"1:17","name":"Hero Secondary Text","type":"TEXT","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#0485b2"}],"absoluteBoundingBox":{"x":320,"y":496,"width":114,"height":19},"characters":"View Our Work","style":{"fontFamily":"Inter","fontStyle":"Medium","fontWeight":500,"fontSize":16,"textAlignHorizontal":"LEFT","letterSpacing":0,"lineHeightPx":19.363636016845703}},{"id":"1:18","name":"Hero Image","type":"FRAME","fills":[{"opacity":0.10000000149011612,"blendMode":"NORMAL","type":"SOLID","color":"#0485b2"}],"cornerRadius":16,"absoluteBoundingBox":{"x":720,"y":120,"width":640,"height":520},"children":[]},{"id":"2:21","name":"Services Label","type":"TEXT","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#0485b2"}],"absoluteBoundingBox":{"x":80,"y":840,"width":87,"height":17},"characters":"Our Services","style":{"fontFamily":"Inter","fontStyle":"Medium","fontWeight":500,"fontSize":14,"textAlignHorizontal":"LEFT","letterSpacing":0,"lineHeightPx":16.94318199157715}},{"id":"2:22","name":"Services Title","type":"TEXT","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#1a1a1a"}],"absoluteBoundingBox":{"x":80,"y":870,"width":390,"height":58},"characters":"What we do best","style":{"fontFamily":"Inter","fontStyle":"Semi Bold","fontWeight":600,"fontSize":48,"textAlignHorizontal":"LEFT","letterSpacing":0,"lineHeightPx":58.09090805053711}},{"id":"4:51","name":"Footer","type":"FRAME","fills":[{"blendMode":"NORMAL","type":"SOLID","color":"#1a1a1a"}],"absoluteBoundingBox":{"x":0,"y":1750,"width":1440,"height":430},"children":[]}]}

def main():
    print("=" * 60)
    print("FIGMA TO ELEMENTOR CONVERSION TEST")
    print("=" * 60)

    # Step 1: Parse Figma data
    print("\n[1] Parsing Figma data...")
    parser = FigmaParser(figma_data)
    parsed = parser.parse()

    print(f"    - Name: {parsed['metadata']['name']}")
    print(f"    - Size: {parsed['metadata']['width']}x{parsed['metadata']['height']}px")
    print(f"    - Elements found: {len(parsed['elements'])}")
    print(f"    - Colors extracted: {len(parsed['design_tokens']['colors'])}")
    print(f"    - Typography styles: {len(parsed['design_tokens']['typography'])}")

    # Step 2: Generate Elementor JSON
    print("\n[2] Generating Elementor JSON...")
    generator = ElementorGenerator(parsed)
    elementor_data = generator.generate()

    print(f"    - Sections created: {len(elementor_data['content'])}")
    print(f"    - Page title: {elementor_data['title']}")

    # Step 3: Save output
    output_path = 'output_elementor_template.json'
    with open(output_path, 'w') as f:
        json.dump(elementor_data, f, indent=2)

    print(f"\n[3] Saved to: {output_path}")

    # Preview
    print("\n" + "=" * 60)
    print("PREVIEW (first 2000 chars):")
    print("=" * 60)
    preview = json.dumps(elementor_data, indent=2)[:2000]
    print(preview)
    print("...")

    print("\n" + "=" * 60)
    print("DESIGN TOKENS EXTRACTED:")
    print("=" * 60)
    print("\nColors:")
    for color, name in parsed['design_tokens']['colors'].items():
        print(f"    {name}: {color}")

    print("\nTypography:")
    for key, typo in list(parsed['design_tokens']['typography'].items())[:5]:
        print(f"    {typo['family']} {typo['size']}px ({typo['weight']})")

    print("\n" + "=" * 60)
    print("SUCCESS! Template ready for import into Elementor")
    print("=" * 60)


if __name__ == '__main__':
    main()
