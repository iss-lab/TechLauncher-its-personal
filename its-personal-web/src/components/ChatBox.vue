<template>
    <div id="chatbot">
      <el-row class="chatbot-wrapper">
        <el-col :span="4" class="sidebar-container">
          <div class="user">
            <img src="../assets/avatar.png" />
            <div style="display: flex; flex-flow: column; align-items: center">
              <span>Eric</span>
              <span style="color: #7d7d7d">eric1998@gmail.com</span>
            </div>
          </div>
          <el-menu
            @open="handleOpen"
            @close="handleClose"
            class="el-menu-vertical-demo"
            default-active="1-1-1"
            :default-openeds="['1', '1-1', '1-2']"
          >
            <el-sub-menu index="1">
              <template #title>
                <span>Topics</span>
              </template>
              <el-sub-menu index="1-1">
                <template #title>Entertaining</template>
                <el-menu-item index="1-1-1" @click="activeIndex = 0"
                  >film</el-menu-item
                >
                <el-menu-item index="1-1-2" @click="activeIndex = 1"
                  >tv</el-menu-item
                >
                <el-menu-item index="1-1-3" @click="activeIndex = 2"
                  >star</el-menu-item
                >
              </el-sub-menu>
              <el-sub-menu index="1-2">
                <template #title>Sports</template>
                <el-menu-item index="1-2-1" @click="activeIndex = 3"
                  >Football</el-menu-item
                >
                <el-menu-item index="1-2-2" @click="activeIndex = 4"
                  >Basketball</el-menu-item
                >
              </el-sub-menu>
            </el-sub-menu>
          </el-menu>
        </el-col>
        <el-col :span="6" class="news-container">
          <div class="news">
            <div v-for="(item, index) in data[activeIndex]" :key="index">
              <img :src="item.img" />
              <div>
                {{ item.title }}
              </div>
            </div>
          </div>
        </el-col>
        <el-col :span="14" class="chatBox">
          <div
            style="
              padding: 20px;
              display: flex;
              height: 100%;
              width: 100%;
              flex-flow: column;
              justify-content: end;
              box-sizing: border-box;
            "
          >
            <div class="message"></div>
            <div class="publish">
              <textarea
                class="text-area placeholder"
                placeholder="Type your message......"
              ></textarea>
              <div class="send">send</div>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
</template>

<script>
import { defineComponent } from "vue";
import { ElRow, ElCol, ElMenu, ElSubMenu, ElMenuItem } from "element-plus";
import "element-plus/dist/index.css";
export default defineComponent({
  name: "chatbot",
  components: {
    ElMenuItem,
    ElMenu,
    ElRow,
    ElCol,
    ElSubMenu
  },
  data() {
    return {
      activeIndex: 0,
      data: [
        [
          {
            title: "123123123123",
            img: require("../assets/news.png"),
          },
          {
            title: "3213123123123",
            img: require("../assets/news.png"),
          },
          {
            title: "234234523423",
            img: require("../assets/news.png"),
          },
          {
            title: "656746345",
            img: require("../assets/news.png"),
          },
          {
            title: "465868769789",
            img: require("../assets/news.png"),
          },
          {
            title: "7868963423423",
            img: require("../assets/news.png"),
          },
        ],
        [
          {
            title: "hgergwefwer",
            img: require("../assets/news.png"),
          },
          {
            title: "thgwerwerwer",
            img: require("../assets/news.png"),
          },
          {
            title: "thtyh45534",
            img: require("../assets/news.png"),
          },
          {
            title: "dfh534g4w3geg",
            img: require("../assets/news.png"),
          },
          {
            title: "3yt4hh45h45t",
            img: require("../assets/news.png"),
          },
          {
            title: "345grthrthrth",
            img: require("../assets/news.png"),
          },
        ],
        [
          {
            title: "g345g34g34g34fsd",
            img: require("../assets/news.png"),
          },
          {
            title: "g5uh56u678564",
            img: require("../assets/news.png"),
          },
          {
            title: "sdfdfg4353545",
            img: require("../assets/news.png"),
          },
          {
            title: "567867854gd",
            img: require("../assets/news.png"),
          },
          {
            title: "3456yghfghfg",
            img: require("../assets/news.png"),
          },
          {
            title: "2345eghdfghfgh",
            img: require("../assets/news.png"),
          },
        ],
        [
          {
            title: "dfg34t34g345g34",
            img: require("../assets/news.png"),
          },
          {
            title: "36y45h4g3e45g34",
            img: require("../assets/news.png"),
          },
          {
            title: "g345g56uh56dfgdf",
            img: require("../assets/news.png"),
          },
          {
            title: "thfsdfsdf3443",
            img: require("../assets/news.png"),
          },
          {
            title: "45htryhtryhrth",
            img: require("../assets/news.png"),
          },
          {
            title: "fghtryrty345345345g",
            img: require("../assets/news.png"),
          },
        ],
        [
          {
            title: "gfhfghwrwr2333",
            img: require("../assets/news.png"),
          },
          {
            title: "iluk57664545",
            img: require("../assets/news.png"),
          },
          {
            title: "fghjfg4546354634",
            img: require("../assets/news.png"),
          },
          {
            title: "fgh454563456",
            img: require("../assets/news.png"),
          },
          {
            title: "sdfsf345345",
            img: require("../assets/news.png"),
          },
          {
            title: "7657rthgrf4535",
            img: require("../assets/news.png"),
          },
        ],
      ],
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
})
</script>

<style scoped lang="scss">
.message {
  flex: 1;
  padding: 15px;
  border: 1px solid #cccccc;
  margin-bottom: 20px;
  border-radius: 10px;
}

.publish {
  display: flex;
  flex-flow: column;
  align-items: end;
}

.text-area {
  padding: 16px 16px 23px;
  width: 100%;
  resize: none;
  background: #f5f5f6;
  border-radius: 12px;
  border: none;
  color: #1f1f1f;
  box-sizing: border-box;
  outline: none;
}

.send {
  margin-top: 15px;
  width: 80px;
  height: 30px;
  line-height: 30px;
  font-size: 14px;
  text-align: center;
  color: #fff;
  background: #4e6ef2;
  border-radius: 15px;
  cursor: pointer;
}

.chatbot-wrapper {
  position: relative;
  height: 100%;
  width: 100%;
}

.chatBox {
  height: 100%;
  overflow: hidden;
}

.news {
  border-right: 1px solid #add8e6;
  height: 100%;
}

.news > div {
  padding: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #add8e6;
}

.news > div img {
  width: 40%;
}

.news > div > div {
  width: 50%;
  height: 100%;
}

.news-container {
  height: 100%;
  overflow-y: scroll;
}

.sidebar-container {
  height: 100%;
  overflow: hidden;
  background-color: #add8e6;
}

.user {
  display: flex;
  justify-content: center;
  flex-flow: column;
  align-items: center;
  padding: 20px 0;
  img {
    width: 80px;
    margin-bottom: 10px;
  }
}

.el-menu {
  height: 100%;
  transition-property: auto !important;
  background-color: #add8e6;
}

.el-sub-menu {
  background-color: #add8e6;
  ::v-deep .el-sub-menu__title {
    color: #ffffff;
    font-weight: bold;
  }
  ::v-deep .el-sub-menu__title:hover {
    color: #2c3e50;
  }
  ::v-deep .el-menu {
    background-color: #add8e6;
    transition-property: auto !important;
    .el-menu-item {
      color: #ffffff;
    }
    .el-menu-item:hover {
      color: #2c3e50;
    }
    .el-menu-item.is-active {
      background-color: #ecf5ff;
      color: #2c3e50;
    }
  }
}
</style>