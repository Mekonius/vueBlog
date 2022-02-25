<template>
  <div class="post" v-if="post">
    <h2>{{ post.title }}: {{ post.subtitle }}</h2>
    By <AuthorLink :author="post.author" />
    <div>{{ displayableDate(post.publishDate) }}</div>
    <p class="post__description">{{ post.metaDescription }}</p>
    <article>
        <img width="200" v-bind:src="'http://127.0.0.1:8000/media/' +  post.image" alt="test" />
        <br />
      {{ post.body }} 
      <ul>
      <li v-for="ingredient in post.ingredients" :key="ingredient.name">
        <div>
        <router-link :to="`/ingredient/${ingredient.name}`">#{{ ingredient.name }}</router-link>
        </div>
      </li>
      </ul>
    </article>
    <ul>
      <li class="post__tags" v-for="tag in post.tags" :key="tag.name">
        <router-link :to="`/tag/${tag.name}`">#{{ tag.name }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import AuthorLink from "../components/AuthorLink.vue";
import gql from "graphql-tag";

export default {
  name: "postItem",
  components: {
    AuthorLink,
  },
  data() {
    return {
      post: null,
    };
  },
  methods: {
    displayableDate(date) {
      return new Intl.DateTimeFormat("en-US", { dateStyle: "full" }).format(
        new Date(date)
      );
    },
  },
  async created() {
    const post = await this.$apollo.query({
      query: gql`
        query ($slug: String!) {
          postBySlug(slug: $slug) {
            title
            subtitle
            publishDate
            metaDescription
            slug
            body
            image
            ingredients{
              name
            }
            author {
              user {
                username
                firstName
                lastName
              }
            }
            tags {
              name
            }
          }
        }
      `,
      variables: {
        slug: this.$route.params.slug,
      },
    });
    this.post = post.data.postBySlug;
  },
};
</script>
