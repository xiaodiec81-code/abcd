import unittest
import sys
import os

# Add the directory to sys.path so we can import the nodes
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from toonflow_nodes import ToonflowAsset, ToonflowAssetGroup, ToonflowPromptBuilder, ToonflowPromptLoader

class TestToonflowNodesV2(unittest.TestCase):
    
    def test_asset_creation(self):
        node = ToonflowAsset()
        name = "TestChar"
        desc = "A test character"
        type_ = "角色"
        
        result = node.create_asset(name, desc, type_)
        asset = result[0]
        
        self.assertEqual(asset["name"], name)
        self.assertEqual(asset["description"], desc)
        self.assertEqual(asset["type"], type_)
        print(f"[PASS] Asset creation successful: {asset}")

    def test_asset_grouping(self):
        group_node = ToonflowAssetGroup()
        
        asset1 = {"name": "A1", "description": "D1", "type": "角色"}
        asset2 = {"name": "A2", "description": "D2", "type": "场景"}
        
        # Test creating a new group
        result = group_node.group_assets(asset_1=asset1, asset_2=asset2)
        group = result[0]
        
        self.assertEqual(len(group), 2)
        self.assertEqual(group[0], asset1)
        self.assertEqual(group[1], asset2)
        print(f"[PASS] Asset grouping successful: {len(group)} assets")
        
        # Test appending to existing group
        asset3 = {"name": "A3", "description": "D3", "type": "道具"}
        result_extended = group_node.group_assets(asset_1=asset3, prev_group=group)
        extended_group = result_extended[0]
        
        self.assertEqual(len(extended_group), 3)
        self.assertEqual(extended_group[0], asset1)
        self.assertEqual(extended_group[2], asset3)
        print(f"[PASS] Asset group extension successful: {len(extended_group)} assets")

    def test_prompt_builder(self):
        builder = ToonflowPromptBuilder()
        loader = ToonflowPromptLoader()
        
        # Load a template
        template = loader.load_prompt("画面提示词优化师")[0]
        
        # Mock inputs
        storyboard = "Character A fights Character B"
        style = "Anime"
        ratio = "16:9"
        assets = [
            {"name": "CharA", "description": "Hero", "type": "角色"},
            {"name": "CharB", "description": "Villain", "type": "角色"}
        ]
        
        result = builder.build_prompt(storyboard, style, ratio, template, assets)
        final_prompt = result[0]
        
        # Verify content
        self.assertIn(template, final_prompt)
        self.assertIn(storyboard, final_prompt)
        self.assertIn("CharA：Hero", final_prompt)
        self.assertIn("CharB：Villain", final_prompt)
        self.assertIn("16:9", final_prompt)
        self.assertIn("Anime", final_prompt)
        
        print(f"[PASS] Prompt builder assembled content correctly")

if __name__ == '__main__':
    unittest.main()
